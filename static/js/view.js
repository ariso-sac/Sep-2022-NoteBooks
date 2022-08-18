const app = new Vue({
    el: "#app",
    data: function () {
        return {
            name:"Hello",
            posts:[]
        }
    },
    async created() {
        // use created for api calls
        const a = await fetch('/api?auth_token=', {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
        })
        const b = await a.json()
        console.log(b)
        b.forEach(element => {
            this.posts.push(element)
        });
    },
    methods: {
        like: function (id) {
            console.log(id);
            const a = fetch('/api/' + id, {
                method: 'PUT',
                mode: 'cors',
            })
            location.reload('/')
        },
    },
    computed: {

    }
})