// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/parent_class.h"
#include "class_name.generated.h"
enum_header
struct_space
UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class project_name_API prefixed_class : public Uparent_class
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	prefixed_class();
	enum_space
protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

		
};
