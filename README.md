# tl;dr
```
make
```

this should create & run a docker image (see it running with `docker ps`).

You should now be able to visit the website at `localhost`.

**note:** I ask docker to assign the yatube container to port 80 here, so if you have something *else* running at port 80 from before, make sure to stop these other applications so that you can have yatube on port 80 instead :), or you can edit the Makefile to assign yatube to a different port on the host machine... :( )

## dependencies

- [Docker](https://www.docker.com/)
- [GNU Make](https://www.gnu.org/software/make/)

# what is this?

yatube is yet another tube.

# features (conceptual):

only allow uploading / publishing videos if they are "cool" enough. Make this an exercise in NNs.
aka, find some videos that are 'cool' (just pick some videos from a competing video tube website that have many views :p, who cares what the contents of the video is! the masses wouldn't watch it if it wasn't "cool" in some way!, use this as training + testing. Use the view count as the "coolness" factor i guess, and have the NN try to estimate the videos "coolness")
