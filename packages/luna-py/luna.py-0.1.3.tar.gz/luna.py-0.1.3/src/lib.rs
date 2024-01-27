mod adapter;
mod node;

use adapter::Adapter;
use node::Node;
use pyo3::prelude::*;

#[pyclass]
struct Engine;

impl Engine {
    fn build_node_tree(message: &str) -> Vec<Node> {
        let mut nodes = Vec::new();
        let mut start_index = None;

        for (i, c) in message.chars().enumerate() {
            match c {
                '{' => start_index = Some(i),
                '}' => {
                    if let Some(start) = start_index {
                        let node_str = &message[start + 1..i];
                        let mut parts = node_str.splitn(2, '(');
                        let variable = parts.next().unwrap_or("");
                        let parameter = parts.next().map(|p| p.trim_end_matches(')'));
                        let raw = match &parameter {
                            Some(param) => format!("{{{}({})}}", &variable, param),
                            None => format!("{{{}}}", &variable),
                        };

                        nodes.push(Node {
                            variable: variable.to_string(),
                            position: (start as u32, i as u32),
                            parameter: parameter.map(String::from),
                            raw,
                        });

                        start_index = None;
                    }
                }
                _ => {}
            }
        }

        nodes
    }
}

#[pymethods]
impl Engine {
    #[staticmethod]
    fn process(message: &str, adapters: Vec<Adapter>) -> String {
        let mut output = String::new();
        let mut last_position = 0;

        let nodes = Engine::build_node_tree(message);

        for node in nodes {
            if let Some(adapter) = adapters
                .iter()
                .find(|a| a.variables.contains(&node.variable))
            {
                let replacement = match node.parameter {
                    Some(parameter) => adapter.attributes.get(&parameter).unwrap_or(&node.raw),
                    None => &adapter.default_attribute,
                };

                output.push_str(&message[last_position..node.position.0 as usize]);
                output.push_str(replacement);
            } else {
                output.push_str(&message[last_position..=node.position.1 as usize]);
            }
            last_position = (node.position.1 + 1) as usize;
        }

        output.push_str(&message[last_position..]);

        output
    }
}

#[pymodule]
fn luna(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Adapter>()?;
    m.add_class::<Engine>()?;
    Ok(())
}
