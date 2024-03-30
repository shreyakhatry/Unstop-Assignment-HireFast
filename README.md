1. Use python3.8
2. Create a virtual environment using the following command:
```bash
python3.8 -m venv venv
```
3. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```
---

To run UI analyzer run the following command, [generate OpenAI key]( https://platform.openai.com/api-keys) and add it to
environment variable OPENAI_API_KEY:
```bash
export OPENAI_API_KEY=<your-key>
streamlit run aicheck.py
```

To run the local natural language processing utility run the following command:
```bash
python analyze.py
```
