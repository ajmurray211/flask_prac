// url= 'mongodb+srv://admin123:0000@cluster0.vzqog5g.mongodb.net/flask_prac?retryWrites=true&w=majority'
url = 'http://127.0.0.1:5000/'

const getName = (event) => {
    event.preventDefault()
    let name = document.getElementById('name').value
    fetch(`http://127.0.0.1:5000/${name}`)
        .then((res) => res.json())
        .then((data) => {
            document.getElementById('output').innerHTML = `<li class="list-group-item"> name: ${data.name}, Genre: ${data.genre}, Game: ${data.game}</li>`
        })
}

document.getElementById('formData').addEventListener('submit', getName)

const postData = (event) => {
    event.preventDefault()
    let name = document.getElementById('postName').value
    let genre = document.getElementById('postGenre').value
    let game = document.getElementById('postGame').value

    fetch('http://127.0.0.1:5000/postData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'name': name,
            'genre': genre,
            'game': game
        })
    })
        .then((res) => res.json())
        .then((data) => console.log(data))
}

document.getElementById('postData').addEventListener('submit', postData)