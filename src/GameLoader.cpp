#include <Windows.h>
//#include <detours.h>

STARTUPINFOW si = { 0 };
PROCESS_INFORMATION pi = { 0 };

INT APIENTRY WinMain(_In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance, _In_ LPSTR lpCmdLine, _In_ int nShowCmd)
{
	si.cb = sizeof(si);
	if (!CreateProcessW(L"Sakika.exe", NULL, NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi))
	{
		MessageBoxW(NULL, L"Get Start Failed!!", NULL, MB_OK);
		return FALSE;
	}

	ResumeThread(pi.hThread);
	CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);

	return TRUE;

}