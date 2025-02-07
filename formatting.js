const fs = require('fs')

fs.readFile('./text.txt', 'utf8', (err, data) => {
    if(err) {
        console.log(err)
    }

    data = data.split('\r')
    q = data.map(function (z) {
        return z.replace('\n', '')
        })

    console.log(q)
    t = q.map(function(a) {
        arr = a.split(' ')
        return arr[arr.length -1]

    })
    console.log(t)
})


//can just split based on ' ' and return last thing btw