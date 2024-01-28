use pyo3::{pyclass, pymethods, PyResult};
use serde::{Deserialize, Serialize};

#[derive(Clone, Serialize, Deserialize)]
#[pyclass]
pub(crate) struct Geolocation {
    #[pyo3(get)]
    altitude: i16,
    #[pyo3(get)]
    latitude: i8,
    #[pyo3(get)]
    longitude: i8,
}

#[derive(Clone, Serialize, Deserialize)]
#[pyclass]
pub(crate) struct SignatureSong {
    #[pyo3(get)]
    samples: u32,
    #[pyo3(get)]
    timestamp: u32,
    #[pyo3(get)]
    uri: String,
}

#[derive(Clone, Serialize, Deserialize)]
#[pyclass]
pub(crate) struct Signature {
    #[pyo3(get)]
    geolocation: Geolocation,
    #[pyo3(get)]
    signature: SignatureSong,
    #[pyo3(get)]
    timestamp: u32,
    #[pyo3(get)]
    timezone: String,
}

#[pymethods]
impl crate::Geolocation {
    #[new]
    pub fn new(
        altitude: i16,
        latitude: i8,
        longitude: i8,
    ) -> PyResult<Self> {
        return Ok(Geolocation { altitude, latitude, longitude });
    }
}

#[pymethods]
impl crate::SignatureSong {
    #[new]
    pub fn new(
        samples: u32,
        timestamp: u32,
        uri: String,
    ) -> PyResult<Self> {
        return Ok(SignatureSong { samples, timestamp, uri });
    }
}


#[pymethods]
impl crate::Signature {
    #[new]
    pub fn new(
        geolocation: Geolocation,
        signature: SignatureSong,
        timestamp: u32,
        timezone: String,
    ) -> PyResult<Self> {
        return Ok(Signature { geolocation, signature, timestamp, timezone });
    }
}