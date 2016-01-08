## Instructions
1. Run `server.py` on the `server` computer you want to accept the conneciton.
2. Once you see the message indicating the server has started you can move to the client.
3. Run `client.py` on the `client` machine and enter the IPv4 address.(e.g. `192.168.1.2`)
    
    a.There is currently no validation on the input, so it must be correct or the client application will just crash and you'll have to rerun it.
4. Once the connection is open, you'll see the message `Connection established` on the client PC and `Connection established from: ` with the client information on the server console. Once this appears the client will be automatically disconnected.