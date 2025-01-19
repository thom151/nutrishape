document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    const sendChatBtn = document.querySelector(".chat-input span");
    sendChatBtn.addEventListener("click", handleChat);

    document.querySelector(".chat-input textarea").addEventListener("keydown", (e) => {
      if(e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleChat();
      }
    });

    document.addEventListener('click', function(event) {
      if (event.target.classList.contains('food-options')) {
        const food_id = event.target.id;
        console.log(food_id);
        getRecipe(food_id);
      }
    });
    
  
  });



function handleChat() {
    const chatInput = document.querySelector(".chat-input textarea");
    let userMessage = chatInput.value;
    if (!userMessage) return;
    const chatbox = document.querySelector(".chatbox");
    chatbox.appendChild(createDiv(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    getResponse(userMessage);
    chatInput.value = "";
}


function createDiv(message, type, called=false) {
  
  if (!called) {
  console.log("no function called");
  const typeDiv = document.createElement("div");
  typeDiv.classList.add("chat", type);
  let chatContent = type === "outgoing" ? `<p>${message}</p>` : `<span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`
  typeDiv.innerHTML = chatContent;
  return typeDiv
  }
  else {
    const chatbox = document.querySelector(".chatbox");
    const typeDiv = document.createElement("div");
    typeDiv.classList.add("chat", type);


    const options = document.createElement("div");
    options.classList.add("options")

    message.forEach((food) => {
      console.log("function called babyyyy");
      console.log(food);

      

      const foodDiv = document.createElement("div");
      foodDiv.classList.add("food-options");
      console.log(food.recipe_id);
      foodDiv.id = food.recipe_id;


      const foodId = document.createElement("input")
      foodId.innerHTML = food.recipe_id;
      foodId.setAttribute("type", "hidden");


      const foodTitle = document.createElement("h2");
      foodTitle.innerHTML = food.recipe_name;

      const foodImg = document.createElement("img");
      foodImg.src= food.recipe_image;

      const foodDesc = document.createElement("div");
      foodDesc.classList.add("options-description");
      foodDesc.innerHTML = food.recipe_description;

      const nutriDetails = document.createElement("ul");
      const cal = document.createElement("li");
      cal.innerHTML = food.recipe_nutrition;
      nutriDetails.appendChild(cal);


      foodDiv.appendChild(foodTitle);
      foodDiv.appendChild(foodImg);
      foodDiv.appendChild(foodDesc);
      foodDiv.appendChild(nutriDetails);
      foodDiv.appendChild(foodId);


      options.appendChild(foodDiv);
      
      });

      typeDiv.appendChild(options);
      return typeDiv;
  }
}


function getResponse(message) {
  event.preventDefault();
  fetch('/chat', {
    method: 'POST',
    body: JSON.stringify({
        message: document.querySelector('.chat-input textarea').value,
        thread : document.querySelector('.thread_id').value
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      if (!result.func_called){ 
      document.querySelector(".thread_id").value = result.thread;
      console.log(result.Response)
      const chatbox = document.querySelector(".chatbox");
      chatbox.appendChild(createDiv(result.Response, "incoming", result.func_called));
      chatbox.scrollTo(0, chatbox.scrollHeight)}
      else {
        document.querySelector(".thread_id").value = result.thread;
        console.log(result.Response)
        console.log("function called")

        const chatbox = document.querySelector(".chatbox")
      
        chatbox.appendChild(createDiv(result.Response, "incoming", result.func_called));
        chatbox.scrollTo(0, chatbox.scrollHeight);
      }
  });
}




function getRecipe(id) {
  event.preventDefault();
  window.location.href = `/getRecipe/${id}`;
}



