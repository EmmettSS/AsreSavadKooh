const  slide_container = document.getElementById('slide_container-index')
const slide = document.querySelectorAll('.slide-index').length

let translate = 100 / slide
let value = 100 / slide
let numb = 0


function checkWidth() {
    var width = window.innerWidth;

    if (width > 600) {
        slide_container.style.width = `${slide * (100 / 4) + 1}%`
        numb = 3
    }

    if (width <= 600) {
        slide_container.style.width = `${slide * (100 / 3) + 1}%`
        numb = 2
    }
}

window.addEventListener('resize', checkWidth);

checkWidth();


setInterval(() => {
   if(slide != 1 & slide != 2 & slide != 3 & slide != 4){
      slide_container.style.transform = `translateX(${value}%)`
      value += translate
   }
   if(value == translate * (slide - numb)){
      value = 0
   }
}, 1800);