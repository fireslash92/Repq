"use strict";
const AetherState=(()=>{
const objectives=["Speak to Elder Mira in Ashwood","Defeat the forest sentinel","Enter the crypt and defeat its guardian","Open the relic chest","Return to Elder Mira","Chapter complete · explore freely"];
const initial=()=>({version:1,stage:0,hp:100,gold:12,potions:3,relic:false,x:0,z:-23,skill:2});
const normalize=v=>{let s=initial();if(v&&v.version===1){for(const k of ["stage","hp","gold","potions","x","z","skill"])if(Number.isFinite(v[k]))s[k]=v[k];s.stage=Math.max(0,Math.min(5,Math.floor(s.stage)));s.hp=Math.max(1,Math.min(100,s.hp));s.potions=Math.max(0,Math.floor(s.potions));s.gold=Math.max(0,Math.floor(s.gold));s.x=Math.max(-23,Math.min(23,s.x));s.z=Math.max(-29,Math.min(54.8,s.z));s.relic=s.stage>=4;s.skill=Math.max(0,Math.min(2,s.skill));}return s;};
const heal=s=>{if(!s.potions||s.hp===100)return false;s.potions--;s.hp=Math.min(100,s.hp+45);return true;};
const accept=s=>{if(s.stage!==0)return false;s.stage=1;return true;};
const win=(s,kind)=>{if(kind==="forest"&&s.stage===1){s.stage=2;s.gold+=18;s.potions++;return true;}if(kind==="crypt"&&s.stage===2){s.stage=3;s.gold+=32;return true;}return false;};
const relic=s=>{if(s.stage!==3)return false;s.stage=4;s.relic=true;s.gold+=20;return true;};
const finish=s=>{if(s.stage!==4)return false;s.stage=5;s.gold+=60;s.hp=100;return true;};
const turn=(s,e,move)=>{if(e.hp<=0)return {ok:false,message:"Encounter is complete."};if(move==="potion"){if(!heal(s))return {ok:false,message:"No potion needed or available."};}else if(move==="skill"){if(!s.skill)return {ok:false,message:"Radiance is exhausted."};s.skill--;e.hp-=34;}else if(move==="attack")e.hp-=20;else if(move!=="guard")return {ok:false,message:"Choose an action."};if(e.hp<=0){e.hp=0;win(s,e.kind);return {ok:true,won:true,damage:0};}let damage=move==="guard"?3:e.kind==="crypt"?19:13;s.hp=Math.max(0,s.hp-damage);if(move==="guard")s.skill=Math.min(2,s.skill+1);return {ok:true,damage,lost:s.hp===0};};
return {initial,normalize,heal,accept,win,relic,finish,turn,objectives};
})();
if(typeof module!=="undefined")module.exports=AetherState;
