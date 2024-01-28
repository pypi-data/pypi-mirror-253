mod fingerprinting;
mod errors;
mod response;

use pyo3::prelude::PyModule;
use pyo3::{ToPyObject, PyErr, pymodule, PyResult, PyObject, Python, pyclass, pymethods};
use fingerprinting::algorithm::SignatureGenerator;
use fingerprinting::communication::get_signature_json;
use crate::errors::SignatureError;
use crate::response::{Geolocation, Signature, SignatureSong};

#[pymodule]
fn shazamio_core(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Recognizer>()?;
    m.add_class::<SignatureError>()?;
    m.add_class::<Geolocation>()?;
    m.add_class::<SignatureSong>()?;
    m.add_class::<Signature>()?;
    Ok(())
}


#[derive(Clone)]
#[pyclass]
struct Recognizer;


#[pymethods]
impl Recognizer {
    #[new]
    pub fn new() -> PyResult<Self> {
        return Ok(Recognizer {});
    }


    fn recognize_path(&self, py: Python, value: String) -> PyResult<PyObject> {
        let future = async move {
            let data = SignatureGenerator::make_signature_from_file(&value)
                .map_err(|e| {
                    let error_message = format!("{}", e);
                    PyErr::new::<SignatureError, _>(SignatureError::new(error_message))
                })?;

            let signature = get_signature_json(&data)
                .map_err(|e| {
                    let error_message = format!("{}", e);
                    PyErr::new::<SignatureError, _>(SignatureError::new(error_message))
                })?;
            return Signature::new(
                Geolocation::new(signature.geolocation.altitude, signature.geolocation.latitude, signature.geolocation.longitude)?,
                SignatureSong::new(signature.signature.samples, signature.signature.timestamp, signature.signature.uri)?,
                signature.timestamp,
                signature.timezone,
            );
        };

        let python_future = pyo3_asyncio::tokio::future_into_py(py, async move {
            tokio::task::spawn_blocking(move || {
                futures::executor::block_on(future)
            }).await.unwrap()
        });

        python_future.map(|any| any.to_object(py))
    }
}
