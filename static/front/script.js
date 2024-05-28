

document.querySelector('#btnmenu').addEventListener('click',()=>{
    if(document.querySelector('#menu').style.right=='-800px'){
    document.querySelector('#menu').style.right='-200px';
    }
    else{
    document.querySelector('#menu').style.right='-800px';
    }
    })
    
    
    document.querySelector('#filter').addEventListener('click',()=>{
    if(document.querySelector('#category').style.display=="none"){
        document.querySelector('#category').style.display="block";
    }
    else{
        document.querySelector('#category').style.display="none";
    }
    })
    
    
    
    document.querySelector('#close').addEventListener('click',()=>{
        document.querySelector('.cart').style.display="none";
    })
    
    document.querySelector('#cart').addEventListener('click',()=>{
        document.querySelector('#menu').style.right='-800px';
        document.querySelector('.cart').style.display="block";
       
    })