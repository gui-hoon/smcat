// JSON 파일 불러오기
function loadCat(){
    return fetch('data/cats.json')
    .then(response => response.json())
    .then(json => json.cats);
}

// 고양이 정보를 목록에 업데이트하기
function displayCats(cats){
    const container = document.querySelector('.cats')
    container.innerHTML = cats.map(cat => createHTMLString(cat)).join('');
}

// 정보를 HTML형식으로 바꾸기
function createHTMLString(cats){
    return `
    <div class="catImg"><img src="${cats.image}" alt="">${cats.name}</div>
    `;
}

// 고양이 정보 불러오기
loadCat()
.then(cats => {
    displayCats(cats);
    setEventListner(cats);
})
.catch(console.log);