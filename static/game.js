async function handleSubmit(evt){
    evt.preventDefault();
    const word = document.querySelector("#guess-input").value 
    let check = await checking(word)
    result = check.data.result
    msg = sortMsg(result)
    showMsg(msg)
    points = score(result,word)
    scoreHtml(points)
    timeOut(stopGuess)
    await axios.post("/post-score",{points : points})   
}


let btn= document.querySelector("#submit")
btn.addEventListener("click", handleSubmit)

async function checking(word){
    let res = axios.get("/check-word", {params:{word:word}})
    return res
}

function showMsg(msg){
    message= document.querySelector("#message")
    message.innerText = msg
    
}
function sortMsg(result){
    
    if(result === "ok"){
        return "valid word"
    }if(result === "not-word"){
        return "not valid Englis word"
    }if(result==="not-on-board"){
        return "not valid word on board"
    }
    
}
let points=0
let guessed =[]
function scoreHtml(points){
    pointsHtml =document.querySelector("#score")
    pointsHtml.innerText = points
}
function score(result,word){
    if(result==="ok" && !guessed.includes(word) ){
        points += word.length
        guessed.push(word)
    }
    return points   
}

function stopGuess(){
    button = document.querySelector("#submit")
    button.disabled = true
}

function timeOut(func1){
    setTimeout(func1 ,60000)
}

