use pyo3::{pyclass, PyErrArguments, pymethods, PyObject, PyResult, Python, ToPyObject};
use pyo3::exceptions::PyException;
use pyo3::types::PyString;

trait BaseException {
    fn __str__(&self) -> PyResult<String>;
    fn __repr__(&self) -> PyResult<String>;
}


#[pyclass(extends = PyException)]
pub struct SignatureError {
    message: String,
}

#[pymethods]
impl SignatureError {
    #[new]
    pub fn new(message: String) -> Self {
        SignatureError { message }
    }
}

impl BaseException for SignatureError {
    fn __str__(&self) -> PyResult<String> {
        Ok(format!("{message}", message = self.message))
    }

    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("SignatureError({message})", message = self.message))
    }
}

impl PyErrArguments for SignatureError {
    fn arguments(self, py: Python) -> PyObject {
        PyString::new(py, &self.message).to_object(py)
    }
}
