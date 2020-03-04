// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/parent_class.h"
#include "class_name.generated.h"

enum_header
struct_space

UCLASS()
class project_name_API prefixed_class : public Aparent_class
{
	GENERATED_BODY()

public:
	// Sets default values for this parent_class's properties
	prefixed_class();
	enum_space
protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

};
