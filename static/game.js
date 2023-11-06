async function handleSubmit(evt){
    evt.preventDefault();
    const word = document.querySelector("#guess-input").value 
    // console.log(word)
    let res = axios.get("/check-word", {params:{word:word}})
    console.log(res)
}


let btn= document.querySelector("#submit")
btn.addEventListener("click", await handleSubmit)

// async function checking(){
//     let res = axios.get("/check-word", {params:{word:word}})
//     console.log(res)
// }