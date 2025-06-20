# RAG ChatBot 🤖🔎

A Retrieval-Augmented Generation (RAG) chatbot built with [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and [Groq Llama 3](https://groq.com/). This bot can hold natural conversations and search the internet for up-to-date information using the Tavily Search Engine tool.

---

## ✨ Features

- **Conversational Chatbot**: Engages in natural, multi-turn dialogue.
- **Internet Search**: Uses the Tavily tool to fetch the latest information from various sources.
- **Retrieval-Augmented Generation (RAG)**: Combines LLM reasoning with real-time search for more accurate and current answers.
- **Modular and Extensible**: Built with LangGraph’s state-based workflow for easy customization and expansion.
- **API Key Integration**: Supports Groq and Tavily APIs for scalable, reliable access to LLMs and web content.

---

## 🚀 Quickstart

### 1. Clone this repo

```bash
git clone https://github.com/Sasi0026/Generative-AI-Engineer.git
cd Generative-AI-Engineer/rag-chatbot
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Add your API keys

Set your API keys for Groq and Tavily. You can either:
- Set them as environment variables before running the script:
  ```bash
  export GROQ_API_KEY="your_groq_api_key"
  export TAVILY_API_KEY="your_tavily_api_key"
  ```
- Or insert them directly in the `app.py` file (not recommended for production).

### 4. Run the chatbot

```bash
python app.py
```

---

## 📝 Example Usage

Ask questions like:

> "Try to give the most recent research papers about humanoid robots, mostly released by Stanford, IIT Bombay, and Kharagpur. List more than 3 papers, only titles and the URLs."

The chatbot will search the internet for up-to-date answers and respond with relevant research paper titles and links.

---

## 🖼️ Example Output / Screenshots

Include screenshots of your Colab or terminal output here to showcase the bot’s capabilities! For example:

![Example response from the chatbot](screenshots/example_response.png![image](https://github.com/user-attachments/assets/84ecbcb7-a456-45ce-87f4-ef8986976b15)
)

Or paste sample output:

```
1. "Stanford Humanoid Advances 2024" - https://arxiv.org/abs/2405.12345
2. "IIT Bombay: Learning-based Control for Humanoids" - https://ieeexplore.ieee.org/document/9876543
3. "IIT Kharagpur: Robust Bipedal Walking" - https://journals.sagepub.com/doi/10.1177/123456789
...
```

---

## 🛠️ Project Structure

```
rag-chatbot/
├── app.py            # Main application code with detailed comments
├── requirements.txt  # Python dependencies
├── README.md         # This file!
└── screenshots/      # Example output, screenshots, etc.
```

---

## 💡 How it Works

- Utilizes a state graph (LangGraph) to manage dialogue and decide when to invoke search tools.
- Integrates Groq’s Llama-3.1-8B-Instant model for intelligent conversation.
- When a question requires internet search, uses TavilySearchResults to fetch and summarize latest data.
- Maintains conversation history using memory checkpoints.

---

## 🙋‍♂️ Contributing

Contributions and suggestions are welcome! Please open an issue or submit a pull request.

---

## 📄 License

[MIT License](../LICENSE)  
© 2025 Sasi0026

---

## 🔗 References

- [LangGraph Documentation](https://langgraph.readthedocs.io/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq Llama3](https://groq.com/products/llama3/)
- [Tavily Search API](https://app.tavily.com/)

