FROM golang:1.16-buster as build

ARG GOPROXY=https://goproxy.cn,direct

WORKDIR /go/src/app
COPY go.mod /go/src/app
COPY go.sum /go/src/app

RUN GOPROXY=${GOPROXY} go mod download

ADD . /go/src/app

RUN GOPROXY=${GOPROXY} go build -o /go/bin/app

# Now copy it into our base image.
FROM dcr.teletraan.io/public/gcr-distroless-static:latest

COPY --from=build /go/bin/app /
