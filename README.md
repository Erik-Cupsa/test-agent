# PromptShop Test Agent

 A simple Python agent for testing PromptShop's agent execution system.

 ## Usage

 This agent reads a prompt from `input.json` and uses OpenAI's GPT-4o-mini to generate a response.

 ### Input Format
 ```json
 {
   "prompt": "Your question or message here"
 }

 Environment Variables

 - OPENAI_API_KEY - Provided automatically by PromptShop during execution

 Local Testing

 pip install -r requirements.txt
 echo '{"prompt": "Hello!"}' > input.json
 OPENAI_API_KEY=your-key python main.py

 ---
## Steps to Test

 1. **Create GitHub repo** named `promptshop-test-agent`
 2. **Add the 3 files** above
 3. **Push to GitHub** (public repo)
 4. **Create listing in PromptShop**:
    - Product type: `agent`
    - Enable execution: `Yes`
    - GitHub repo URL: `https://github.com/YOUR_USERNAME/promptshop-test-agent`
    - Runtime: `Python`
    - Entrypoint: `main.py`
    - AI Model: `OpenAI`
    - Add input field:
      - Name: `prompt`
      - Type: `textarea`
      - Label: `Your prompt`
      - Required: `Yes`
 5. **Submit for review**
 6. **Test via Admin panel**:
    - Go to Admin > Listings
    - Find the test agent
    - Click "Test Agent"
    - Enter a test prompt
    - Click "Run Test"
    - Verify stdout shows the AI response

 ---

 ## Expected Test Output

 Received prompt: What is 2+2?

 --- AI Response ---
 2 + 2 = 4
 ```
