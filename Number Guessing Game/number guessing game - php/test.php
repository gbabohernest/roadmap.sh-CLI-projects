#!/usr/bin/env php

<?php




function main() : void {

    echo "Enter a number: ";
    fscanf(STDIN, "%d", $num);

    if ($num) {
        echo "The number you entered is $num\n";
        return;
    }

    echo "You entered something that is not a number\n";
}


main();









