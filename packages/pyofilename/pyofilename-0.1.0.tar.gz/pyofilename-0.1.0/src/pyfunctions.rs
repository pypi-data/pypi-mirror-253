use pyo3::{exceptions::PyValueError, prelude::*};
use crate::functions;
use crate::components::*;

#[pyfunction]
pub fn is_name_reserved(name: &str, strict: Option<bool>) -> bool {
    functions::is_name_reserved(name, strict.unwrap_or(true))
}

#[pyfunction]
pub fn is_safe_name(name: &str, only_check_creatable: Option<bool>, strict: Option<bool>) -> bool {
    functions::is_safe_name(name, only_check_creatable.unwrap_or(false), strict.unwrap_or(true))
}

#[pyfunction]
pub fn to_safe_name(
    name: &str,
    replace_method: &str,
    replace_char: Option<char>,
    dot_handling_policy: Option<&str>,
    strict: Option<bool>,
) -> PyResult<String> {
    let replace_method = match replace_method {
        "fullwidth" => ReplaceMethod::Fullwidth(ReplaceChar::Charactor(replace_char.unwrap_or('_'))),
        "replace" => ReplaceMethod::Replace(ReplaceChar::Charactor(replace_char.unwrap_or('_'))),
        "remove" => ReplaceMethod::Remove,
        invalid_option => return Err(PyErr::new::<PyValueError, _>(format!("Invalid option : `{}`.", invalid_option))),
    };
    let dot_handling_policy = match dot_handling_policy {
        Some(policy) => match policy {
            "remove" => DotHandlingPolicy::Remove,
            "replace" => DotHandlingPolicy::ReplaceWithReplaceMethod,
            "not_correct" => DotHandlingPolicy::NotCorrect,
            invalid_option => return Err(PyErr::new::<PyValueError, _>(format!("Invalid option : `{}`.", invalid_option))),
        },
        None => DotHandlingPolicy::ReplaceWithReplaceMethod
    };
    Ok(functions::to_safe_name(name, replace_method.compile(), dot_handling_policy, strict.unwrap_or(true)))
}