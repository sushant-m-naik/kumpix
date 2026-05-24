// f = open("usr.db")

async function jo() {


    // lnk = document.location.host + "/op.txt"
    const response = await fetch("db");
    const text = await response.json();
    confirm(text)
    confirm(response)
    // confirm(lnk)


}

// jo()


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

        document.getElementById('jok').innerHTML = ""
        var d = document.createElement("p")
        d.id="joki"
        var acc= localStorage
        d.innerHTML = `${acc.Name}
                    
                    ${acc.Email}
        `
        document.getElementById('jok').append(d)
        // alert("hi")
        var follower= document.getElementById('jok')
        var k= follower.offsetWidth
        k=parseInt(k)
        document.onmousemove= (e) => {
            
            // document.getElementById('jok').style.display = 'block'
            document.getElementById('joki').style.opacity = '1'
            document.getElementById('joki').style.padding = '10px'
            follower.style.left = (e.pageX-(k+10) )+`px`;
            follower.style.top = (e.pageY-7)+`px`;
        }
    })
    op.onmouseout = () => {
        document.getElementById('joki').style.opacity = '0'
        document.getElementById('joki').style.padding = '0px'
        document.getElementById('joki').remove()


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
    var lst = localStorage
    lst.clear()
    lst.setItem("Name", nm)
    lst.setItem("Email", em)
    
    // document.location="/"

}
