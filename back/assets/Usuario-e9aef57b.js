import{r as p,A as u,d as f,o as n,c,e as a,b as d}from"./index-34bd876b.js";const m=a("h2",null,"Hola",-1),h=["src"],g={__name:"Usuario_Componente",setup(s){const o=p(""),i=u().get_api_host,r=f.create({baseURL:i});function l(){let t={current_user_page:window.location.pathname};r.post("api/profile-pic",t=t).then(function(e){console.log(e),o.value=e.data.profile_pic_src}).catch(function(e){console.log(e)}).finally(function(){console.log("profile_pic_url =",o.value)})}return l(),(t,e)=>(n(),c("div",null,[a("div",null,[m,a("img",{src:o.value},null,8,h)])]))}},x={__name:"Usuario",setup(s){return(o,_)=>(n(),c("main",null,[d(g)]))}};export{x as default};
