// url= 'mongodb+srv://admin123:0000@cluster0.vzqog5g.mongodb.net/flask_prac?retryWrites=true&w=majority'
url= 'http://127.0.0.1:5000/'

const getName = (event) =>{
    event.preventDefault()
    
    let name = document.getElementById('name').value
    
    fetch(`http://127.0.0.1:5000/${name}`)
    .then((res) => res.json())
    .then((data) => {
        document.getElementById('output').innerHTML = `name: ${data.name}, Genre: ${data.genre}, Game: ${data.game}`
    })
}
document.getElementById('formData').addEventListener('submit', getName)