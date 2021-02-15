#!/bin/bash
source ../env/bin/activate
daphne dndPartyManager.asgi:application
