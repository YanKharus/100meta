const fs = require('fs').promises;


async function  LPDataFormatting() {
    try{
    const rawTextData = await fs.readFile('./text.txt', 'utf8')
        
    let data = rawTextData.split('\r')
        
    let q = data.map(function (z) {
        return z.replace('\n', '')
        })

    let formattedLP = q.map(function(a) {
        arr = a.split(' ')
        return arr[arr.length -1]   
        })
        
    return formattedLP
}   
catch(error){
    console.error(error)}
}

async function nameDataFormatting() {
    try{
        const currentDate = new Date();
        const formattedDate = currentDate.toLocaleDateString();
    
        const rawTextData = await fs.readFile('./names.txt', 'utf8')
            
        let data = rawTextData.split('\r')

        let q = data.map(function (z) {
            return z.replace('\n', '')
            })
        return q
        
    }   
    catch(error){
        console.error(error)}
}


async function playerData() {
    const date = new Date()
    const formattedDate = date.toLocaleDateString()
    let name = await nameDataFormatting()
    let LP = await LPDataFormatting()
    let players = {}
    for (let i = 0; i < LP.length; i++) {
        players[name[i]] = {
        rank: i + 1,
        LP: LP[i],
        lastSeen: formattedDate}
    }
    console.log(...Object.keys(players))
}

playerData()
/* back to thinking about how im gonna group all the information together. within this stage of the process I will have my laptop
send requests to gather PUUIDs and group it in as a property for each person how am I gonna do the list of names thing to the 
worker dyno? I feel like I need to actually get my hands on it and see how it works and what Ill have it do before I even bother
using it maybe I should just have a prototype of examples using tft as an example and see if my laptop could handle it*/



 // check if the process untouched leaves a random newline after OCR in text.txt and how consistent it is if it does
 /* since the positions should mirror each other (should as in can updates randomly occur in the middle of my process? if
 things randomly update theres no way I can catch it because OCR cant read special characters, I have to leave that portion
 for the name loop can OCR the banner name and get LP. the issue with being wishy washy if somehow a lot of changes occur
 and someone is recorded to have more LP than they actually did and that is saved for highest recorded it feels like the 
 difference cant be that high. because its someone else moving in or out of the way so the position moves once except for
 if theres a plataeu between players and )
 what is the worst thing that can happen in this case? a mismatch for 1-100 LP and a single position change most likely? 
 it doesnt matter that much but still something Ill remember for now
 I can just get them both in a 100 index array and have a loop build an object with the playername time taken and current rank
 + current LP */