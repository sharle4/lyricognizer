const getLyrics = require("./getLyrics")
const getSong = require("./getSong")
const title_given = process.argv[2]
const options = {
    apiKey:'jusEv8f-8DSL_Ys2wh0dvdqO3Ld3KodYMmuHqMBWIfeMyg80EZTwvz07-CVP3Gvq',
    title: title_given ,
    artist:'nekfeu',
    opitmizeQuery:true,

}
getLyrics(options).then((lyrics)=>console.log(lyrics));
getSong(options).then((song)=>
    console.log(
        `${song.lyrics}`)


)