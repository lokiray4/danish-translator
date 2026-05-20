async function upload(){

const file=
document.getElementById(
"video"
).files[0]

const formData=
new FormData()

formData.append(
"file",
file
)

const response=
await fetch(
"后面替换",
{
method:"POST",
body:formData
}
)

const data=
await response.json()

document.getElementById(
"result"
).innerHTML=
`
<h3>丹麦语</h3>
${data.danish}

<h3>中文</h3>
${data.translation}
`
}
