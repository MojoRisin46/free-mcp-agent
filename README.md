# MCP LLM Agent Testing Framework

A minimal, flexible system to experiment with LLMs, model settings, and MCP (Model Context Protocol) behavior — without relying on pre-made templates.

---

## 📜 Project Overview

### Current State
- **Hard Reads**: The agent is forced to read predefined contexts — it does not decide autonomously what to read.
- **Tooling**: Tools defined in the MCP server are not yet being utilized.
- **Test Data**: Using random motorsports data and text contexts to test LLM responses under varying parameters.

### Purpose
- Build a **free and flexible test environment** for experimenting with different models, temperatures, and settings.
- Understand **how a bare-bones MCP implementation works** from scratch — no boilerplate or templates.
- Provide a base for further agentic system development.

---

## ⚙️ How to Recreate

1. **Initialize Environment**
   ```bash
   uv init


2. **Sync Dependencies**

   ```bash
   uv sync
   ```

3. **Get a GitHub Token**

   * Generate a token via: [GitHub Settings → Tokens](https://github.com/settings/tokens)
   * Place it into your `.env` file.

4. **Run the MCP Server**

   ```bash
   uv run scripts/mcp_server.py
   ```

5. **Run the LLM Agent**

   ```bash
   uv run scripts/llm_agent.py
   ```

6. **Modify Settings**

   * Change the context, model, temperature, etc., directly in the code.

---

## 🤖 Model Selection

Refer to the GitHub Marketplace for available models.
Example — Mistral model:
[AzureML Mistral Medium 2505](https://github.com/marketplace/models/azureml-mistral/mistral-medium-2505)

---

## 🙏 Acknowledgements

* Massive help by **ChatGPT** in setting up MCP and connections.
* **GitHub Marketplace** for providing model integration options.

---

## 🚀 Future Plans

* Add tools via **Tool Bridge**.
* Implement **human-like memory** for persistent agent behavior.
* Enable **multi-agent interactions**.

---

## 📂 Project Structure

* `scripts/` — Python scripts for MCP server and LLM agent.
* `docs/` — draw.io and svg of the project structure
* `data/` — Test datasets (currently motorsports data).
* `app/` — Application-related code (if applicable).
* `.env` — Contains API keys and environment variables.
* `pyproject.toml` — Project configuration and dependencies.
* `uv.lock` — Dependency lock file.
* `README.md`

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
