"use strict";(self["webpackChunklogistics"]=self["webpackChunklogistics"]||[]).push([[272],{38880:(e,t,r)=>{var s=r(82109),o=r(47293),n=r(45656),l=r(31236).f,a=r(19781),i=!a||o((function(){l(1)}));s({target:"Object",stat:!0,forced:i,sham:!a},{getOwnPropertyDescriptor:function(e,t){return l(n(e),t)}})},52272:(e,t,r)=>{r.r(t),r.d(t,{default:()=>P});var s=r(73396),o=r(35010),n=r(87139),l=r(66949),a={class:"flex w-full font-base flex-col lg:justify-center lg:items-center"},i={class:"lg:mt-32 mt-6 text-center font-base bg-white lg:pb-20 pb-10 mx-2 lg:mx-0 lg:w-1/2 max-w-lg rounded-xl"},u=(0,s._)("div",{class:"flex items-center justify-center"},[(0,s._)("img",{src:l,class:"h-32 w-32 rounded-full object-cover",alt:""})],-1),c=(0,s._)("h3",{class:"text-3xl font-bold"},"Welcome back",-1),d=(0,s._)("p",{class:"text-sm text-gray-600 mt-3"},"Please enter your details to log in",-1),p={class:"flex mt-5 text-start flex-col gap-2 mr-5 ml-5"},m=(0,s._)("label",{for:"email",class:"text-gray-800 text-sm"},"Email address",-1),g={key:0,class:"text-red-500"},f={class:"flex mt-5 text-start flex-col gap-2 mr-5 ml-5"},b=(0,s._)("label",{for:"password",class:"text-gray-800 text-sm"},"Password",-1),w={key:0,class:"text-red-500"},x=(0,s._)("div",{class:"flex justify-end text-violet-600 underline text-sm mt-2"},[(0,s._)("a",{href:"/reset"},"Forgot password?")],-1),y={class:"mr-5 ml-5 mt-5 flex lg:flex-row flex-col gap-5"},h=(0,s._)("div",{class:"flex justify-center text-violet-600 gap-2 mt-5 text-sm"},[(0,s._)("p",{class:"text-gray-800"},"Don't have an account?"),(0,s.Uk)(),(0,s._)("a",{href:"#"},"Request one")],-1);function v(e,t,r,l,v,O){return(0,s.wg)(),(0,s.iD)("div",a,[(0,s._)("form",i,[u,c,d,(0,s._)("div",p,[m,(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[0]||(t[0]=function(e){return v.user.email=e}),type:"email",class:"border border-gray-200 shadow-sm focus:ring-0 focus:outline-none bg-white py-2 rounded-md pl-4",placeholder:"Enter your email"},null,512),[[o.nr,v.user.email]]),v.emailError?((0,s.wg)(),(0,s.iD)("small",g,(0,n.zw)(v.errorMessage),1)):(0,s.kq)("",!0)]),(0,s._)("div",f,[b,(0,s.wy)((0,s._)("input",{"onUpdate:modelValue":t[1]||(t[1]=function(e){return v.user.password=e}),type:"password",class:"border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm",placeholder:"********"},null,512),[[o.nr,v.user.password]]),v.passwordError?((0,s.wg)(),(0,s.iD)("small",w,(0,n.zw)(v.errorMessage),1)):(0,s.kq)("",!0),x]),(0,s._)("div",y,[(0,s._)("button",{onClick:t[2]||(t[2]=(0,o.iM)((function(){return O.submitLoginRequest&&O.submitLoginRequest.apply(O,arguments)}),["prevent"])),class:"bg-violet-600 w-full text-white py-2 px-12 rounded-md"},"Log in"),(0,s._)("button",{onClick:t[3]||(t[3]=(0,o.iM)((function(){return O.submitGuestLoginRequest&&O.submitGuestLoginRequest.apply(O,arguments)}),["prevent"])),class:"bg-violet-600 w-full text-white py-2 px-12 rounded-md"},"Guest log in")]),h])])}var O=r(95082),_=(r(57658),r(26699),r(32023),r(32564),r(20065));const j={name:"Login",data:function(){return{user:{email:"",password:""},emailError:!1,passwordError:!1,errorMessage:""}},methods:(0,O.Z)((0,O.Z)((0,O.Z)({},(0,_.nv)({loginUser:"loginUser"})),(0,_.OI)({})),{},{submitLoginRequest:function(){var e=this;this.loginUser({payload:this.user,cb:function(t){e.$router.push({name:"dashboard"})},errorCb:function(t){t.response.data.detail.includes("password")&&(e.passwordError=!0,e.errorMessage=t.response.data.detail,setTimeout((function(){return e.passwordError=!1}),2e3)),t.response.data.detail.includes("user")&&(e.emailError=!0,e.errorMessage=t.response.data.detail,setTimeout((function(){return e.emailError=!1}),2e3))}})},submitGuestLoginRequest:function(){this.user={email:"nick@gmail.com",password:"33992433nkl"},this.submitLoginRequest()}})};var k=r(40089);const E=(0,k.Z)(j,[["render",v]]),P=E},66949:(e,t,r)=>{e.exports=r.p+"img/logo.042a1363.png"},95082:(e,t,r)=>{r.d(t,{Z:()=>n});r(47941),r(82526),r(57327),r(41539),r(38880),r(57658),r(89554),r(54747),r(49337),r(33321),r(69070);var s=r(82482);function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);t&&(s=s.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,s)}return r}function n(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){(0,s.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}}}]);
//# sourceMappingURL=272.a13be2b9.js.map