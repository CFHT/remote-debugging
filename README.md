
### Demo1
1 Start the docker instance

```bash
docker run -dit -p 2222:22 cfht/remote-debugging
```
2 Use [sshfs](sshfs-project) to mount the code:

```bash
mkdir -p ~/mnt
sshfs circleci@localhost:/app/ -p 2222  ~/mnt
```

3 Then open the tunnel for debugging
```bash
ssh -R 1234:localhost:1234 circleci@localhost -p 2222
```

4 Open up py-charm, and load a new project at `~/mnt/app`

5 Create a new configuration, select python remote debug.

6 Set the port to 1234

7 Add the import pydevd and listen lines from the configuration page.

8 Run the configuration

9. run `sudo pip install pydevd`

10. Run `demo1.sh`



[sshfs-project]: https://github.com/libfuse/sshfs
