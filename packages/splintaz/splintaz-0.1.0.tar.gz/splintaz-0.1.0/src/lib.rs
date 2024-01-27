use pyo3::prelude::*;

mod splinters;

use splinters::calculate_fracture_surface;

/// A Python module implemented in Rust.
#[pymodule]
fn splintaz(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_fracture_surface, m)?)?;
    Ok(())
}
