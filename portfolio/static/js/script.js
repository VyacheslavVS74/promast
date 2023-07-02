"use strict"

/*=====================Header======================*/
const menu = document.querySelector('.menu__body')
const menuBtn = document.querySelector('.menu__icon')

const body = document.body;

if (menu && menuBtn) {
	menuBtn.addEventListener('click', e => {
		menu.classList.toggle('active')
		menuBtn.classList.toggle('active')
		body.classList.toggle('lock')
	})

	menu.addEventListener('click', e => {
		if (e.target.classList.contains('menu__body')) {
			menu.classList.remove('active')
			menuBtn.classList.remove('active')
			body.classList.remove('lock')
		}
	})

	menu.querySelectorAll('.menu__link').forEach(link => {
		link.addEventListener('click', () => {
			menu.classList.remove('active')
			menuBtn.classList.remove('active')
			body.classList.remove('lock')
		})
	})
}

/*===========================================*/

const anchors = document.querySelectorAll('a[href*="#"]');

anchors.forEach(anchor => {
	anchor.addEventListener('click', event => {
		event.preventDefault();

		const blockID = anchor.getAttribute('href').substring(1);

		document.getElementById(blockID).scrollIntoView({
			behavior: 'smooth',
			block: 'start'
		})
	})
})
/*=====================/Header======================*/

/*=====================Slider======================*/




let offset = 0;
let imageWork = document.getElementsByClassName('image-work-main').length;
const sliderLine = document.querySelector('.slider-line');

if (window.innerWidth >= 581){
	if (imageWork == 3) {
		document.querySelector('.slider-next').addEventListener('click', function(){
			offset = offset + 450;
			if (offset > 900) {
				offset = 0
			}
			sliderLine.style.left = -offset + 'px'
		});
		
		document.querySelector('.slider-prev').addEventListener('click', function(){
			offset = offset - 450;
			if (offset < 0) {
				offset = 900
			}
			sliderLine.style.left = -offset + 'px'
		});
		}
		console.log(imageWork)
		
		if (imageWork == 2) {
			document.querySelector('.slider-next').addEventListener('click', function(){
				offset = offset + 450;
				if (offset > 450) {
					offset = 0
				}
				sliderLine.style.left = -offset + 'px'
			});
			
			document.querySelector('.slider-prev').addEventListener('click', function(){
				offset = offset - 450;
				if (offset < 0) {
					offset = 450
				}
				sliderLine.style.left = -offset + 'px'
			});
			}
			console.log(imageWork)
		
			if (imageWork == 1) {
					const buttonPrev = document.querySelector('.slider-prev')
					const buttonNext = document.querySelector('.slider-next')
					buttonPrev.style.display = 'none'
					buttonNext.style.display = 'none'
				}
}
else {
	if (imageWork == 3) {
		document.querySelector('.slider-next').addEventListener('click', function(){
			offset = offset + 300;
			if (offset > 600) {
				offset = 0
			}
			sliderLine.style.left = -offset + 'px'
		});
		
		document.querySelector('.slider-prev').addEventListener('click', function(){
			offset = offset - 300;
			if (offset < 0) {
				offset = 600
			}
			sliderLine.style.left = -offset + 'px'
		});
		}
		console.log(imageWork)
		
		if (imageWork == 2) {
			document.querySelector('.slider-next').addEventListener('click', function(){
				offset = offset + 300;
				if (offset > 300) {
					offset = 0
				}
				sliderLine.style.left = -offset + 'px'
			});
			
			document.querySelector('.slider-prev').addEventListener('click', function(){
				offset = offset - 300;
				if (offset < 0) {
					offset = 300
				}
				sliderLine.style.left = -offset + 'px'
			});
			}
			console.log(imageWork)
		
			if (imageWork == 1) {
					const buttonPrev = document.querySelector('.slider-prev')
					const buttonNext = document.querySelector('.slider-next')
					buttonPrev.style.display = 'none'
					buttonNext.style.display = 'none'
				}
}

/*=====================/Slider======================*/

/*=====================Pagination======================*/

let searchForm = document.getElementById('search')
let pageLink = document.querySelectorAll('.page-link')

if (searchForm) {
  for (let i = 0; pageLink.length > i; i++) {
    pageLink[i].addEventListener('click', function (e) {
      e.preventDefault()

      let page = this.dataset.page;
      searchForm.innerHTML += `<input value=${page} name="page" type="hidden">`
      searchForm.submit();
    })
  }
}
/*=====================/Pagination======================*/