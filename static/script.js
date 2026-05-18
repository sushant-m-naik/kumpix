// f = open("usr.db")

async function jo() {


    // lnk = document.location.host + "/op.txt"
    const response = await fetch("db");
    const text = await response.json();
    confirm(text)
    confirm(response)
    // confirm(lnk)


}

jo()


function loading(){
    var acc= localStorage
    if (acc.Name=='undefined' && acc.Email=='undefined'){
        document.location="/profile"
    }
}


function proff() {
    console.log("i")
    const op = document.getElementById('profile');
    op.addEventListener('mouseover', () => {

        document.getElementById('jok').innerHTML = "hi kok"
        var d = document.createElement("p")
        var acc= localStorage
        d.innerHTML = `${acc.Name}
                    <br>
                    ${acc.Email}
        `
        document.getElementById('jok').append(d)
        // alert("hi")
        var follower= document.getElementById('jok')
        var k= follower.width
        document.onmousemove= (e) => {

            follower.style.left = (e.pageX-100 )+`px`;
            follower.style.top = (e.pageY-7)+`px`;
        }
    })
    op.onmouseout = () => {
        document.getElementById('jok').innerHTML = ""
    }
    // var follower=document.createElement("p")
    // document.append(follower)
    // follower.innerHtml="Hi"
    // }
}


// alert("hi")
function info(inf) {
    alert(inf)
}

function prof(nm, em) {
    // confirm("Your name is: "+nm)
    // confirm("Your email is: "+em)
    document.location="/profile"
    var lst = localStorage
    lst.clear()
    lst.setItem("Name", nm)
    lst.setItem("Email", em)
    

}
