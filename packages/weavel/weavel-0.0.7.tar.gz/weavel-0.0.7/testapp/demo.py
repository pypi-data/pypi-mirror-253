from weavel import create_client

client = create_client()

user_uuid = client.create_user_uuid()

trace_id = client.start_trace(user_uuid)

second_trace_id = client.start_trace(user_uuid)

client.log.system_message(trace_id, "you are a helpful assistant.", unit_name="testapp")

client.log.system_message(second_trace_id, "you are a helpful assistant.")

from openai import OpenAI
openai_client = OpenAI()

user_message = "what can you do for me?"
client.log.user_message(trace_id, user_message, unit_name="testapp")

client.log.user_message(second_trace_id, "hello!", unit_name="second_testapp")
client.log.assistant_message(second_trace_id, "I can help you with a variety of tasks.", unit_name="second_testapp")

# res = openai_client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": user_message}
#     ]
# )

res = "I can assist you with a variety of tasks. I can help answer questions, provide information, give suggestions, assist with research, set reminders, manage your schedule, make reservations, provide translations, and much more. Just let me know what you need help with!"

# print(res.choices[0].message.content)

client.log.assistant_message(trace_id, res, unit_name="test_assistant")

client.add_metadata_to_trace(trace_id, {"user_name": "John Doe"})

client.close()