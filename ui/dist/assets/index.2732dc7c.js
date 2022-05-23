import{r as v,o as g,c as y,a as s,b as c,w as d,T as E,d as L,e as O,p as A,f as T,g as u,h as I,i as P,j as S}from"./vendor.dd02f02e.js";const R=function(){const a=document.createElement("link").relList;if(a&&a.supports&&a.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))o(e);new MutationObserver(e=>{for(const r of e)if(r.type==="childList")for(const t of r.addedNodes)t.tagName==="LINK"&&t.rel==="modulepreload"&&o(t)}).observe(document,{childList:!0,subtree:!0});function i(e){const r={};return e.integrity&&(r.integrity=e.integrity),e.referrerpolicy&&(r.referrerPolicy=e.referrerpolicy),e.crossorigin==="use-credentials"?r.credentials="include":e.crossorigin==="anonymous"?r.credentials="omit":r.credentials="same-origin",r}function o(e){if(e.ep)return;e.ep=!0;const r=i(e);fetch(e.href,r)}};R();const $={default:"#dadbdc",dark:"#2a3036"},x={default:"#dc0000"},C={default:"#607cd8"},D={default:"#64aa67"},V={default:"#8b8c91",dark:"#8e92a3"},B={default:"#E3E7EB",dark:"hsla(0,0%,100%,0.1)"},N={default:"-webkit-linear-gradient(0deg, var(--red), #4b00ed)",dark:"-webkit-linear-gradient(0deg, var(--red), #4545ed)"};var _={"light-background":{default:"#f3f7fb",dark:"#21262a"},"text-main":{default:"#181c2f",dark:"#fff"},border:$,"default-container-background":{default:"#fff",dark:"#16191c"},red:x,blue:C,green:D,disabled:V,hover:B,"disabled-contrast":{default:"rgba(255, 255, 255, 0.5)",dark:"rgba(0, 0, 0, 0.5)"},gradient:N},j="/assets/favicon.492a8e5f.png";var H=(n,a)=>{const i=n.__vccOpts||n;for(const[o,e]of a)i[o]=e;return i};const m="theme";window.getThemes=()=>(window.themes=Object.keys(_[Object.keys(_)[0]]),window.themes);window.getCurrentTheme=()=>window.localStorage.getItem(m)||"default";window.setTheme=n=>{if(!!window.getThemes().includes(n)){window.localStorage.setItem(m,n);for(const a of Object.keys(_))document.documentElement.style.setProperty(`--${a}`,_[a][n]||_[a].default)}};window.setTheme(window.localStorage.getItem(m)||"default");const W={},h=n=>(A("data-v-227ef21f"),n=n(),T(),n),q={id:"appWrapper"},K={class:"header"},M={class:"title"},F=h(()=>s("img",{src:j},null,-1)),G=u("curious"),U=h(()=>s("span",{class:"accent"},"LiDAR",-1)),Y={class:"links"},z=u("Home"),J=u("Control"),Q=u("Table"),X=u("Maintenance"),Z={class:"view"},ee=h(()=>s("div",{class:"lowerHome"},[s("div",{class:"bottomWrapper"},[s("p",null,"A project realised for our B\xFCP"),s("p",null,"\xA9 2022 | David Dias Horta, Paul Meier")])],-1));function te(n,a,i,o,e,r){const t=v("RouterLink"),f=v("router-view");return g(),y("div",q,[s("div",K,[s("div",M,[F,c(t,{class:"rLink noBorder",to:"/"},{default:d(()=>[G,U]),_:1})]),s("div",Y,[c(t,{class:"rLink",to:"/"},{default:d(()=>[z]),_:1}),c(t,{class:"rLink",to:"/control"},{default:d(()=>[J]),_:1}),c(t,{class:"rLink",to:"/table"},{default:d(()=>[Q]),_:1}),c(t,{class:"rLink",to:"/maintenance"},{default:d(()=>[X]),_:1})])]),s("div",Z,[c(f,null,{default:d(({Component:p,route:b})=>[c(E,{name:"slide-fade"},{default:d(()=>[(g(),L(O(p),{key:b.path}))]),_:2},1024)]),_:1})]),ee])}var oe=H(W,[["render",te],["__scopeId","data-v-227ef21f"]]);const re="modulepreload",k={},ne="/",l=function(a,i){return!i||i.length===0?a():Promise.all(i.map(o=>{if(o=`${ne}${o}`,o in k)return;k[o]=!0;const e=o.endsWith(".css"),r=e?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${o}"]${r}`))return;const t=document.createElement("link");if(t.rel=e?"stylesheet":re,e||(t.as="script",t.crossOrigin=""),t.href=o,document.head.appendChild(t),e)return new Promise((f,p)=>{t.addEventListener("load",f),t.addEventListener("error",()=>p(new Error(`Unable to preload CSS for ${o}`)))})})).then(()=>a())},ae=I({history:P("/"),routes:[{path:"/",name:"home",component:()=>l(()=>import("./Home.ca285a96.js"),["assets/Home.ca285a96.js","assets/Home.998a055d.css","assets/vendor.dd02f02e.js"])},{path:"/control",name:"control",component:()=>l(()=>import("./CombinedControl.df232008.js"),["assets/CombinedControl.df232008.js","assets/CombinedControl.f42fd8f5.css","assets/vendor.dd02f02e.js","assets/Graph.ad0af655.js","assets/Graph.b14c5894.css"])},{path:"/graph",name:"graph",component:()=>l(()=>import("./Graph.ad0af655.js"),["assets/Graph.ad0af655.js","assets/Graph.b14c5894.css","assets/vendor.dd02f02e.js"])},{path:"/maintenance",name:"maintenance",component:()=>l(()=>import("./Maintenance.0c43fb37.js"),["assets/Maintenance.0c43fb37.js","assets/Maintenance.3b580f34.css","assets/vendor.dd02f02e.js"])},{path:"/table",name:"table",component:()=>l(()=>import("./Table.428a3fb0.js"),["assets/Table.428a3fb0.js","assets/Table.bba945f4.css","assets/vendor.dd02f02e.js"])}]}),w=S(oe);w.use(ae);w.mount("#app");export{H as _};
