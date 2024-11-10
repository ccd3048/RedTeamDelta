Firewall trolling is my first basic Red tool, it very simply runs indefinitely and opens a firewall rule to the red team subnet
on 50 second intervals, without the use of crontab. this forces the blue teams to monitor the firewall rules as well as active processes


Kudzu is a suite of C2's im in the process of developing.

Kudzu will utilize a single main windows host which is opened to the red team network.
From this windows host, the linux boxes will run the kudzu relay programs, which accept shell commands from the windows host,
thus appearing as if the commands are coming from an internal address, completely  mitigating any rules the blue team has below the router level.
