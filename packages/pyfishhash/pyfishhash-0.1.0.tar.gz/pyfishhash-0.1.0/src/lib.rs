use pyo3::{prelude::*, types::PyBytes};
use std::sync::Mutex;
use once_cell::sync::Lazy;


static FISH_HASH_CONTEXT: Lazy<Mutex<fish_hash::Context>> = Lazy::new(|| {
    let  context = fish_hash::Context::new(false);
    Mutex::new(context)
});


#[pyfunction]
fn hash(_py: Python, input: &PyBytes) -> PyResult<PyObject> {
    // Lock the global context for the duration of the hash operation
    let mut output = [0u8; 32];
    
    fish_hash::hash(&mut output, &mut FISH_HASH_CONTEXT.lock().unwrap(), &input.as_bytes());
    
    Ok(PyBytes::new(_py, &output).into())
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyfishhash(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hash, m)?)?;
    Ok(())
}
