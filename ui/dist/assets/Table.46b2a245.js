import{_}from"./index.4d073236.js";import{j as i,o as a,c as n,F as l,x as p,a as o,y as c}from"./vendor.f11c9b41.js";const u=i({name:"Table",data(){const t=[];for(let e=0;e<360;e++)t.push(360-e);const s=()=>{!this.$router.currentRoute.value.path.includes("table")||(fetch("/data").then(e=>e.json()).then(e=>this.distances=e),setTimeout(s,500))};return s(),{distances:t}}}),m={class:"wrapper"},f={class:"angle"},h={class:"distance"};function v(t,s,e,b,y,$){return a(),n("div",m,[(a(!0),n(l,null,p(t.distances,(d,r)=>(a(),n("div",{class:"row",key:r},[o("span",f,c(r)+" \xB0",1),o("span",h,c(d)+" mm",1)]))),128))])}var B=_(u,[["render",v],["__scopeId","data-v-0cd3cbda"]]);export{B as default};
