  const searchForm = document.querySelector('.search-input');
  const posts = document.querySelectorAll('.title');

  searchForm.addEventListener('keyup',(e)=>{
    Array.from(posts).forEach((post)=>{
      if(post.textContent.toLowerCase().includes(searchForm.value.toLowerCase())){
        post.parentElement.parentElement.style.display='block';
      }
      else{
        post.parentElement.parentElement.style.display='none';
      }
    })
  })