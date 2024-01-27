use pyo3::prelude::*;
use pyo3::types::PyType;
use std::collections::HashMap;

fn add_attr(
    py: Python,
    class: &PyObject,
    attr_name: &str,
    class_attr_name: &str,
    attrs: &mut HashMap<String, String>,
) -> PyResult<()> {
    attrs.insert(
        attr_name.to_string(),
        class
            .getattr(py, class_attr_name)?
            .call_method(py, "__str__", (), None)?
            .extract::<String>(py)?,
    );

    Ok(())
}

fn add_datetime_attr(
    py: Python,
    class: &PyObject,
    attr_name: &str,
    class_attr_name: &str,
    attrs: &mut HashMap<String, String>,
) -> PyResult<()> {
    attrs.insert(
        attr_name.to_string(),
        format!(
            "<t:{}:F>",
            class
                .getattr(py, class_attr_name)?
                .call_method(py, "timestamp", (), None)?
                .extract::<f32>(py)? as u32
        ),
    );

    Ok(())
}

#[pyclass]
#[derive(FromPyObject)]
#[pyo3(get_all)]
pub struct Adapter {
    pub variables: Vec<String>,
    pub default_attribute: String,
    pub attributes: HashMap<String, String>,
}

#[pymethods]
impl Adapter {
    #[classmethod]
    #[rustfmt::skip]
    fn from_member(_cls: &PyType, py: Python, member: PyObject) -> PyResult<Self> {
        let variables = vec![String::from("member"), String::from("user")];

        let mut attributes = HashMap::new();

        add_attr(py, &member, "id", "id", &mut attributes)?;
        add_attr(py, &member, "discriminator", "discriminator", &mut attributes)?;
        add_attr(py, &member, "name", "display_name", &mut attributes)?;
        add_attr(py, &member, "nick", "display_name", &mut attributes)?;
        add_attr(py, &member, "avatar", "display_avatar", &mut attributes)?;
        add_attr(py, &member, "mention", "mention", &mut attributes)?;
        add_attr(py, &member, "color", "color", &mut attributes)?;
        add_attr(py, &member, "bot", "bot", &mut attributes)?;
        add_datetime_attr(py, &member, "created_at", "created_at", &mut attributes)?;
        add_datetime_attr(py, &member, "joined_at", "joined_at", &mut attributes)?;

        Ok(Adapter {
            variables,
            default_attribute: attributes
                .get("name")
                .unwrap_or(&String::from("No Name"))
                .clone(),
            attributes,
        })
    }

    #[classmethod]
    fn from_server(_cls: &PyType, py: Python, server: PyObject) -> PyResult<Self> {
        let variables = vec![String::from("server"), String::from("guild")];

        let mut attributes = HashMap::new();

        add_attr(py, &server, "id", "id", &mut attributes)?;
        add_attr(py, &server, "name", "name", &mut attributes)?;
        add_attr(py, &server, "description", "description", &mut attributes)?;
        add_attr(
            py,
            &server,
            "boosts",
            "premium_subscription_count",
            &mut attributes,
        )?;
        add_attr(py, &server, "icon", "icon", &mut attributes)?;
        add_attr(py, &server, "member_count", "member_count", &mut attributes)?;
        add_attr(py, &server, "members", "member_count", &mut attributes)?;
        add_datetime_attr(py, &server, "created_at", "created_at", &mut attributes)?;

        Ok(Adapter {
            variables,
            default_attribute: attributes
                .get("name")
                .unwrap_or(&String::from("No Name"))
                .clone(),
            attributes,
        })
    }

    #[classmethod]
    fn from_channel(_cls: &PyType, py: Python, channel: PyObject) -> PyResult<Self> {
        let variables = vec![String::from("channel")];

        let mut attributes = HashMap::new();

        add_attr(py, &channel, "id", "id", &mut attributes)?;
        add_attr(py, &channel, "name", "name", &mut attributes)?;
        add_attr(py, &channel, "is_nsfw", "nsfw", &mut attributes)?;
        add_attr(py, &channel, "mention", "mention", &mut attributes)?;
        add_attr(py, &channel, "topic", "topic", &mut attributes)?;
        add_datetime_attr(py, &channel, "created_at", "created_at", &mut attributes)?;

        Ok(Adapter {
            variables,
            default_attribute: attributes
                .get("name")
                .unwrap_or(&String::from("No Name"))
                .clone(),
            attributes,
        })
    }
}
