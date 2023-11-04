import fontstyle
import openai
openai.api_key = "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"
messages = [{'role':'system','content':"you are a intelligent assistant."}]
while True:
    message = input(fontstyle.apply("Mr suraj ask:-","impact/blue/bold"))
    if message == "exit":
        print(fontstyle.apply("Bye Mr suraj","bold/love"))
        break
    else:
        messages.append({'role':'user','content':message},)
        chat=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=messages
            )
        reply=chat.choices[0].message.content
        print(fontstyle.apply(f"devil:-{reply}","bold/impact/green"))
        messages.append({"role":"assistant","content":reply})
        