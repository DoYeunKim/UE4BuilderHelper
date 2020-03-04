// Fill out your copyright notice in the Description page of Project Settings.


#include "include_path/class_name.h"

// Sets default values for this component's properties
prefixed_class::prefixed_class()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	// ...
}


// Called when the game starts
void prefixed_class::BeginPlay()
{
	Super::BeginPlay();

	// ...
	
}


// Called every frame
void prefixed_class::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	// ...
}

