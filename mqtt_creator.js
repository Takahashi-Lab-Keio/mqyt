class Mqtt{
    constructor(data) {
        this.data = data;
        this.broker = 'ws://broker.emqx.io:8083/mqtt';
    }
    subscriber(topic) { //シンプルにsubsbribeしたい場合のメソッド
        console.log("subscribe");
        var client = mqtt.connect(
            this.broker
        );
        client.subscribe(topic);
        client.on('message', function(topic, message){
            console.log('subscriber.on.message', 'topic:', topic, 'message:', message.toString());
            return message.toString()
        });
    }
    subscriber_fetch(topic_fetch) { //subscribeし更にfetchしたい場合のメソッド
        console.log("subscribe");
        var client = mqtt.connect(
            this.broker
        );
        client.subscribe(topic_fetch);
        client.on('message', function(topic_fetch, message){
            console.log('subscriber.on.message', 'topic:', topic_fetch, 'message:', message.toString());
            this.data = {
                content : message.toString()
            };
            console.log("insert前",this.data);
            fetch("/insertDB", { method: 'POST', 
                         headers: { 'Content-Type': 'application/json' }, 
                         body: JSON.stringify({action_list: this.data})})
            .catch(error => {
                console.error('Error!', error.message)});
            
            setTimeout("location.reload()", 300)
        });
    }
    subscriber_img(topic_img) { //subscribeし更にfetchしたい場合のメソッド
        var elem = document.getElementById("image01");
        var client = mqtt.connect(
            this.broker
        );
        client.subscribe(topic_img);
        client.on('message', function(topic_img, message){
            console.log("subscribe img");
            // console.log('subscriber.img', 'topic:', topic_img, 'message:', message.toString());
            elem.src = message.toString();
        });
    }
    publisher(topic,message) {
        var client = mqtt.connect(
            this.broker
        );
        console.log("publish",message);
        client.publish(topic,message);
    }
}
