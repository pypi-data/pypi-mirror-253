use pyo3::prelude::*;
pub mod components;
pub mod functions;
pub mod pyfunctions;

/// A Python module implemented in Rust.
#[pymodule]
fn pyofilename(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pyfunctions::is_name_reserved, m)?)?;
    m.add_function(wrap_pyfunction!(pyfunctions::is_safe_name, m)?)?;
    m.add_function(wrap_pyfunction!(pyfunctions::to_safe_name, m)?)?;
    m.add("NOT_ALLOWED_NAMES_WIN11", components::NOT_ALLOWED_NAMES_WIN11)?;
    m.add("NOT_ALLOWED_NAMES", components::NOT_ALLOWED_NAMES)?;
    m.add("NOT_ALLOWED_CHARS", components::NOT_ALLOWED_CHARS)?;
    Ok(())
}
