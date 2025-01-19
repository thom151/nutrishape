from openai import OpenAI
import json
from dotenv import load_dotenv
from fatsecret import Fatsecret

client = OpenAI(
    api_key=load_dotenv("OPENAI_API_KEY"))


def main():
    newThread = createThread()
    while True:
        message = input("> ")
        if message.lower() == "stop":
            break
        response = sendMessage(message, newThread)
        jsone = toJson(response["bot_response"])
        print(jsone)


def spitRecipe(food, id="", mealType="Lunch"):
    fs = Fatsecret("25646bccc8c64c21bc699163396c5911",
                   "0ac376dd7d3443c2a81686a0265c1e9c")
    # foods = fs.foods_search(food)

    params = {
        "search_expression": food,
        "recipe_type": mealType,
    }

    if id:
        print("there's an id")
        recipe = fs.recipe_get(id)
    else:
        recipe = fs.recipes_search(**params)
    # recipe_id = fs.recipe_get(162)
    return recipe


def fsRecipe(id):
    fs = Fatsecret("25646bccc8c64c21bc699163396c5911",
                   "0ac376dd7d3443c2a81686a0265c1e9c")
    recipe = fs.recipe_get(id)
    return recipe


def sendMessage(message, thread_id):
    called = False
    assistant_id = "asst_Xr5ns1ceuYPhlKns6RMYUMoE"
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )
    print("message_sent")

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    print("run created")

    while True:
        print("running")
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        if run.status == "completed":
            print("completing...")
            messages = client.beta.threads.messages.list(
                thread_id=thread_id
            )
            return {"bot_response": messages.data[0].content[0].text.value, "function_called": called}

        elif run.status == "requires_action":
            print("requires action")
            # parse the data
            called = True
            required_actions = run.required_action.submit_tool_outputs.model_dump()
            tools_output = []
            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])
                print(arguments)
                if func_name == "spitRecipe":
                    print("calling function")
                    try:
                        output = spitRecipe(arguments["food"], arguments["id"])
                        print(output)
                    except KeyError:
                        output = spitRecipe(arguments["food"])
                        print(output)
                    tools_output.append({
                        "tool_call_id": action['id'],
                        "output": json.dumps(output)
                    })
                else:
                    raise ValueError(f"uknown function")
            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tools_output
            )


def giveDailyCal(act_level, sex, age, height, weight, goal="lW", weekly_goal=3500, daily=550):

    # handle BMR for male or female
    if sex.lower() == "male":
        BMR = 10 * int(weight) + 6.25 * int(height) - 5 * int(age) + 5
    elif sex.lower == "female":
        BMR = 10 * int(weight) + 6.25 * int(height) - 5 * int(age) - 161

    # handle activity level
    act = act_level.lower()
    if act == "S":
        TDEE = BMR*1.2
    elif act == "LA":
        TDEE = BMR*1.375
    elif act == "MA":
        TDEE = BMR*1.55
    elif act == "VA":
        TDEE = BMR * 1.725
    else:
        TDEE = BMR*1.9

    # return daily calorie consumption
    return TDEE - daily


# returns a bool weather allergens, type of meal and calories are given and prep time as well
def condGiven():
    pass


def createThread():
    return client.beta.threads.create().id


def toJson(message):
    message = message.replace("```json", "")
    message = message.replace("```", "")
    message = message.replace("\n", "")
    return message


def manageJson(message):
    pass


if __name__ == "__main__":
    main()
