# import os
# import openai
# import gradio as gr

# if you have OpenAI API key as an environment variable, enable the below
# openai.api_key = os.getenv("OPENAI_API_KEY")

# #if you have OpenAI API key as a string, enable the below
# openai.api_key = "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"

# start_sequence = "\nAI:"
# restart_sequence = "\nHuman: "

# prompt = ""

# def openai_create(prompt):

#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     temperature=0.9,
#     max_tokens=150,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0.6,
#     stop=[" Human:", " AI:"]
#     )

#     return response.choices[0].text



# def chatgpt_clone(input, history):
#     history = history or []
#     s = list(sum(history, ()))
#     s.append(input)
#     inp = ' '.join(s)
#     output = openai_create(inp)
#     history.append((input, output))
#     return history, history


# block = gr.Blocks()


# with block:
#     gr.Markdown("""
#     """)
#     chatbot = gr.Chatbot()
#     message = gr.Textbox(placeholder=prompt)
#     state = gr.State()
#     submit = gr.Button("SEND")
#     submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
# block.launch(share=True)
import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)