
async function gettasks(){
    const response = await fetch('http://127.0.0.1:8000/tasks');
    const tasks = await response.json();
    let htmlElementsTitle =
            document.getElementsByClassName("title");
    let htmlElementsContent =
            document.getElementsByClassName("content");
            let htmlElementsTime =
            document.getElementsByClassName("time_alloted");
 
    for (let i = 0; i < htmlElementsTitle.length; i++) {
        console.log(tasks[i].title);
        htmlElementsTitle[i].innerHTML = tasks[i].title;
        
        }
    for (let i = 0; i < htmlElementsContent.length; i++) {
        console.log(tasks[i].content);
        htmlElementsContent[i].innerHTML = tasks[i].content;
        console.log(tasks[i].content);
        }
    for (let i = 0; i < htmlElementsTime.length; i++) {
        console.log(tasks[i].time_alloted);
        htmlElementsTime[i].innerHTML = tasks[i].time_alloted;
        console.log(tasks[i].time_alloted);
        }
}
async function posttask(title, content, time_alloted){
    fetch("http://127.0.0.1:8000/tasks", {
    method: "POST",
    body: JSON.stringify({
        title: title,
        content: content,
        time_alloted: time_alloted
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
})
.then(response => response.json())
.then(json => console.log(json));
}


gettasks();





