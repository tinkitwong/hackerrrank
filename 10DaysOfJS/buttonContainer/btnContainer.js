const container = document.createElement("div");
container.className = "btnContainer";
container.id = "btns";

var buttons = [...Array(9)].map((btn, index, btns) => {
     btns[index] = document.createElement("Button");
     btns[index].id = 'btn' + (index + 1);
     btns[index].innerHTML = (index + 1);
     btns[index].className = "btn";
     container.appendChild(btns[index]);
     return btns[index];
}); 

document.body.appendChild(container);

/** Logic to rotate innerHTML*/
const btn5 = document.getElementById("btn5");

const labels = [1,4,7,8,9,6,3,2];

console.log(buttons.length, labels.length)
function rotate() {
  // let currentLabel = +(btn.innerHTML);
  // get next label
  let nextLabel = labels.pop();
  // update labels
  labels.unshift(nextLabel);
  // update buttons
	for (let i=0; i<4;i++) {
    buttons[i].innerHTML = labels[i]
  }
  for (let i=4; i<labels.length;i++) {
    buttons[i+1].innerHTML = labels[i]
  }
} 

btn5.addEventListener("click", rotate);

