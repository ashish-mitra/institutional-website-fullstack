const myslide = document.querySelectorAll('.myslide');

let counter = 1;
slidefun(counter);

let timer = setInterval(autoSlide, 8000);
function autoSlide() {
	counter += 1;
	slidefun(counter);
}

function resetTimer() {
	clearInterval(timer);
	timer = setInterval(autoSlide, 8000);
}

function slidefun(n) {
	
	let i;
	for(i = 0;i<myslide.length;i++){
		myslide[i].style.display = "none";
	}
	
	if(n > myslide.length){
	   counter = 1;
	   }
	if(n < 1){
	   counter = myslide.length;
	   }
	myslide[counter - 1].style.display = "block";
	
}



// numsection javascript 



var numSecVisible = false;

function checkVisibility() {
    if (!numSecVisible) {
        var numSec = document.getElementById("num-sec");
        var bounding = numSec.getBoundingClientRect();

        if (
            bounding.top >= 0 &&
            bounding.left >= 0 &&
            bounding.right <= (window.innerWidth || document.documentElement.clientWidth) &&
            bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)
        ) {
            let num = document.querySelectorAll('.numbers');
            let time = 4000;
            num.forEach((numelement) => {
                let start = 0;
                let end = parseInt(numelement.getAttribute('data-value'));
                let duration = Math.floor(time / end);
                let counter = setInterval(() => {
                    start += 1;
                    numelement.textContent = start;
                    if (start == end) {
                        clearInterval(counter);
                    }
                }, duration);

            });
            numSecVisible = true;
        }
    }
}

document.addEventListener("DOMContentLoaded", checkVisibility); 
document.addEventListener("scroll", checkVisibility); 


// animation

const observer = new IntersectionObserver ((entries) => {
    entries.forEach((entry) => {
    console.log(entry)
    if (entry.isIntersecting) {
    entry.target.classList.add('show');
    } else {
    entry.target.classList.remove('show');
    }
    });
    });
    const hiddenElements = document.querySelectorAll('.hidden');
    hiddenElements.forEach((el) => observer.observe(el));

    // slide animation
const slidr = new IntersectionObserver ((ent) => {
    ent.forEach((enp) => {
    console.log(enp)
    if (enp.isIntersecting) {
    enp.target.classList.add('slide-show');
    } else {
    enp.target.classList.remove('slide-show');
    }
    });
    });
    const hidden = document.querySelectorAll('.slide-hidden');
    hidden.forEach((el) => slidr.observe(el));
    