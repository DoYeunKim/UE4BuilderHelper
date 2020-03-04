// Fill out your copyright notice in the Description page of Project Settings.


#include "include_path/class_name.h"

// Sets default values
prefixed_class::prefixed_class()
{
 	// Set this parent_class to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void prefixed_class::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void prefixed_class::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void prefixed_class::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

