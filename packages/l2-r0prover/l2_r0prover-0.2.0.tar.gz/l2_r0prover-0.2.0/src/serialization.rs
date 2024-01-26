use anyhow::anyhow;
use pyo3::types::PyBytes;
use pyo3::{PyObject, PyResult, Python, ToPyObject};
use serde::de::DeserializeOwned;
use serde::Serialize;

// The code here that implements pickle for PyO3 classes comes from
//   https://github.com/rth/vtext
// which is under Apache 2.0.
//
// And it is related to this issue in PyO3:
//   https://github.com/PyO3/pyo3/issues/100

pub trait Pickleable: Serialize + DeserializeOwned + Clone {
    fn to_bytes(&self, py: Python<'_>) -> PyResult<PyObject> {
        let bytes = bincode::serialize(&self).map_err(|e| anyhow!("failed to serialize: {}", e))?;
        Ok(PyBytes::new(py, &bytes).to_object(py))
    }

    fn from_bytes(state: PyObject, py: Python<'_>) -> PyResult<Self> {
        match state.extract::<&PyBytes>(py) {
            Ok(s) => {
                let res: Self = bincode::deserialize(s.as_bytes())
                    .map_err(|e| anyhow!("failed to deserialize: {}", e))?;
                Ok(res)
            }
            Err(e) => Err(anyhow!("failed to parse the pickled data as bytes: {}", e).into()),
        }
    }
}
