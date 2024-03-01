import chat_ai as ai


response = ai.start_chat("Lotus", "Phoenix")
print(response)
print(response.text)
print(response.candidates[0].finish_reason.name)
while(True):
    response = ai.send_message_with_image(input('What do you want to say'))
    print(response.text)